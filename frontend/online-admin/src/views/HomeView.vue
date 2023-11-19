<template>
  <div id="home">
    <el-container>
      <el-affix>
        <el-aside>
          <AdminMenu></AdminMenu>
        </el-aside>
      </el-affix>
      <el-container>
<!--        <el-affix>-->
<!--          <el-header class="head">-->
<!--            <AdminHeader></AdminHeader>-->
<!--          </el-header>-->
<!--        </el-affix>-->
        <el-container>
          <el-header class="breadcrumb">
            <AdminBreadcrumb></AdminBreadcrumb>
          </el-header>
          <el-main>
            <RouterView></RouterView>
          </el-main>
        </el-container>
        <!-- <el-main>
          <RouterView></RouterView>
        </el-main> -->
      </el-container>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import AdminHeader from '@/components/layout/AdminHeader.vue'
import AdminMenu from '@/components/layout/AdminMenu.vue'
import AdminBreadcrumb from '@/components/layout/AdminBreadcrumb.vue'
import { useUserInfoStore } from '@/stores/userinfo.store'

const userInfoStore = useUserInfoStore()
</script>

<style lang="scss" scoped>
#home {
  min-height: 100vh;
}

.head {
  background-color: #0f1921;
  padding: 0;
  height: 60px;
}

.el-aside {
  background-color: #0f1921;
  width: 300px;
  height: 100%;
  min-height: 100vh;
  .el-menu-vertical-demo {
    --font-size: 10px;
  };
  //min-height: calc(100vh - 60px);
  //text
}

.breadcrumb {
  background-color: #fff;
  padding-left: 20px;
  height: 26px;
  margin-top: 5px;
}

.el-main {
  max-width: calc(100vw - 210px);
}
</style>
