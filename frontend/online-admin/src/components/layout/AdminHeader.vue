<template>
  <div id="header">
    <div class="right-box">
      <div class="title" style="margin-bottom: 20px; margin-left: 20px"></div>
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
