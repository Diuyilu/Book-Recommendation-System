<template>
  <div id="header">
    <div class="logo-box">中国传媒大学</div>
    <div class="right-box">
      <div class="title">图书推荐系统</div>
      <div class="avater-box">
        <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style lang="scss" scoped>
#header {
  background-color: #2b2c44;
  color: #fff;
  display: flex;
  justify-content: space-between;

  .logo-box {
    width: 200px;
    text-align: center;
    line-height: 60px;
    font-size: 22px;
    font-weight: bold;
    color: #e73267;
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
