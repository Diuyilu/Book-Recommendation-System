<template>
  <div id="header">
    <div class="logo-box">
      <el-image :src=cuclogo fit="fill" style="max-width: 180px;" />
    </div>
    <div class="right-box">
      <div class="title" style="margin-bottom: 20px;margin-left: 20px;">图书个性化推荐系统</div>
      <div class="avater-box">
        <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import cuclogo from '../../assets/cuclogo1.png'
</script>

<style lang="scss" scoped>
#header {
  background-color: #0f1921;
  color: #fff;
  display: flex;
  justify-content: space-between;

  .logo-box {
    width: 200px;
    text-align: center;
    line-height: 60px;
    font-size: 22px;
    font-weight: bold;
    color: #fff;
  }

  .right-box {
    flex: 1;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 18px;

    .el-avatar {
      margin-right: 10px;
    }
  }
}
</style>
