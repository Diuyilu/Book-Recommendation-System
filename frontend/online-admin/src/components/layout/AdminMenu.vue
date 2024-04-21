<template>
  <el-row class="tac">
    <el-image :src="cuclogo" fit="fill" style="width: 95%" />
    <el-col :span="24">
      <el-menu active-text-color="#ffd04b" background-color="#0f1921" class="el-menu-vertical-demo"
        :default-active="defaultActive" text-color="#fff" router @open="handleOpen" @close="handleClose">
        <component :is="item.children ? ElSubMenu : ElMenuItem" v-for="item in menulist" :key="item.id"
          :index="item.index">
          <template v-if="item.children" #title>
            <el-icon v-if="item.icon">
              <component :is="item.icon"></component>
            </el-icon>
            <span style="font-size: 18px">{{ item.name }}</span>
          </template>
          <span v-if="!item.children">
            <el-icon v-if="item.icon">
              <component :is="item.icon"></component>
            </el-icon>
            <span style="font-size: 18px">{{ item.name }}</span>
          </span>
          <el-menu-item style="font-size: 18px" v-for="subItem in item.children" :key="subItem.id"
            :index="subItem.index">
            {{ subItem.name }}
          </el-menu-item>
        </component>
      </el-menu>
    </el-col>
  </el-row>
</template>

<script setup lang="ts">
import type { Component } from 'vue'
import cuclogo from '../../assets/cuclogo1.png'
import { House, User, Platform, Collection, MessageBox } from '@element-plus/icons-vue'
import { ElSubMenu, ElMenuItem } from 'element-plus'
import { ref } from 'vue'
import router from '@/router'
const defaultActive = ref<string>(router.currentRoute.value.path)
interface MenuItem {
  id: number
  name: string
  index: string
  icon?: Component
  children?: MenuItem[]
}
const menulist: MenuItem[] = [
  {
    id: 1,
    name: '首页',
    index: '/home/admin-home',
    icon: House
  },
  // {
  //   id: 2,
  //   name: '数据大屏',
  //   index: '/home/datav',
  //   icon: Platform
  // },
  {
    id: 3,
    name: '个人中心',
    index: '/home/users',
    icon: User,
    children: [
      {
        id: 301,
        name: '借阅历史',
        index: '/home/users/history'
      },
      {
        id: 302,
        name: '个人推荐',
        index: '/home/users/recommend'
      },
      {
        id: 303,
        name: '我的收藏',
        index: '/home/users/collection'
      }
    ]
  },
  {
    id: 4,
    name: '全部书籍',
    index: '/home/books',
    icon: Collection,
    children: [
      {
        id: 401,
        name: '图书检索',
        icon: Collection,
        index: '/home/books/booksearch'
      },
      {
        id: 402,
        name: '新书速递',
        icon: Collection,
        index: '/home/books/newbook'
      },
      {
        id: 403,
        name: '热门书籍',
        icon: Collection,
        index: '/home/books/popularbook'
      },
      {
        id: 404,
        name: '图书分类',
        icon: Collection,
        index: '/home/books/bookclass'
      }
    ]
  }

  // {
  //   id: 5,
  //   name: '图书信息',
  //   icon: MessageBox,
  //   index: '/home/bookinfo'
  // }
]
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>

<style lang="scss" scoped></style>
;
