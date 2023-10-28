<template>
  <!-- <div>recommend</div> -->
  <div>
    <el-form :inline="true" :model="form" label-width="120px">
      <el-form-item label="学号">
        <el-input v-model="form.number" placeholder="请输入学号" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">搜索</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
  <div>
    <el-image style="width: 300px; height: 300px" :src="url" :fit="fill" />
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue'
const form = reactive({
  number: ''
})

const url = 'https://images.weserv.nl/?url=img1.doubanio.com/view/subject/l/public/s29659688.jpg'
const fill = 'contain'
const onSubmit = () => {
  console.log('submit!')
}
</script>

<style lang="scss" scoped>
.el-row {
  margin-bottom: 20px;
}
</style>
