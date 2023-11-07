<template>
  <div id="home">
    <el-container>
      <el-header>
        <AdminHeader></AdminHeader>
      </el-header>
      <el-container>
        <el-affix>
          <el-aside width="200px">
            <AdminMenu></AdminMenu>
          </el-aside>
        </el-affix>
        <el-main>
          <RouterView></RouterView>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import AdminHeader from '@/components/layout/AdminHeader.vue'
import AdminMenu from '@/components/layout/AdminMenu.vue'
import { useUserInfoStore } from '@/stores/userinfo.store';

const userInfoStore = useUserInfoStore()
</script>

<style lang="scss" scoped>
#home {
  min-height: 100vh;
}

.el-header {
  background-color: #2b2c43;
  padding: 0;
}

.el-aside {
  background-color: #2b2c43;
  min-height: calc(100vh - 60px);
}
</style>
