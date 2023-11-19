<template>
  <div class="wrap">
    <statistic-card class="analysis"></statistic-card>
  </div>
</template>

<script setup lang="ts">
import StatisticCard from './adminHome/Statistic.vue'
</script>

<style lang="scss" scoped>
.wrap {
  display: flex;
  flex-wrap: wrap;
  box-shadow: var(--el-box-shadow-light);
  .analysis{
    width: 100%;
    //height: calc((100vh - 130px) / 2);
  }
  //.item {
  //  width: 50%;
  //  height: calc((100vh - 130px) / 2);
  //  min-height: 360px;
  //  padding: 20px;
  //  border: 1px solid #f5f5f5;
  //}
}
</style>
