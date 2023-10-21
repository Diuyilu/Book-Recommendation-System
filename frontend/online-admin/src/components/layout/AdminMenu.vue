<template>
  <div id="menu">
    <el-menu
      active-text-color="#fff"
      background-color="#2b2c44"
      class="el-menu-vertical-demo"
      :default-active="defaultActive"
      text-color="#c1c1c1"
      router
      @open="handleOpen"
      @close="handleClose"
    >
      <component
        :is="item.children ? ElSubMenu : ElMenuItem"
        v-for="item in menulist"
        :key="item.id"
        :index="item.index"
      >
        <template v-if="item.children" #title>
          <el-icon v-if="item.icon">
            <component :is="item.icon"></component>
          </el-icon>
          <span>{{ item.name }}</span>
        </template>
        <span v-if="!item.children">
          <el-icon v-if="item.icon">
            <component :is="item.icon"></component>
          </el-icon>
          <span>{{ item.name }}</span>
        </span>
        <el-menu-item v-for="subItem in item.children" :key="subItem.id" :index="subItem.index">
          {{ subItem.name }}
        </el-menu-item>
      </component>
    </el-menu>
  </div>
</template>

<script setup lang="ts">
import type { Component } from 'vue'
import { House, User, Platform } from '@element-plus/icons-vue'
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
  {
    id: 2,
    name: '数据大屏',
    index: '/home/datav',
    icon: Platform
  },
  {
    id: 3,
    name: '个人中心',
    index: '/home/users',
    icon: User,
    children: [
      {
        id: 101,
        name: '借阅历史',
        index: '/home/history'
      },
      {
        id: 102,
        name: '个人推荐',
        index: '/home/books'
      }
    ]
  }
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
