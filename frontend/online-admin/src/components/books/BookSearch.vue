<template>
    <div id="search">
        <el-form :inline="true" :model="form">
            <el-form-item prop="value">
                <el-input class="input" v-model="form.value" placeholder="请输入书名、作者等书籍信息" />
            </el-form-item>
            <el-form-item prop="button">
                <el-button type="primary" class="btn" @click="search_book_info">搜索</el-button>
            </el-form-item>
        </el-form>
    </div>
    <!-- <el-table :data="tableData" style="width: 100%"> -->
    <el-table :data="message" style="width: 100%">
        <el-table-column prop="book_title" label="书籍名称"></el-table-column>
        <el-table-column label="书籍封面">
            <template #default="scope">
                <div style="display: flex; align-items: center">
                    <el-image :src="scope.row.image_address" style="height:100px ;" />
                </div>
            </template>
        </el-table-column>
        <el-table-column prop="author" label="作者"></el-table-column>
        <el-table-column prop="press" label="出版社"></el-table-column>
        <el-table-column prop="label" label="书籍类型"></el-table-column>
    </el-table>
</template>
  
<script setup lang="ts">
import { ref } from 'vue'
import { getBookInfoAPI, searchBookInfoAPI } from '@/apis/books'

interface Form {
    value: string
}
const form = ref<Form>({
    value: ""
})

const message = ref()

const get_book_info = async () => {
    const res = await getBookInfoAPI()
    console.log(res.book_list)
    message.value = res.book_list
}

const search_book_info = async () => {
    const res = await searchBookInfoAPI(form.value)
    console.log(res.book_list)
    message.value = res.book_list
}

</script>
  
<style lang="scss" scoped>
#search {
    display: flex;
    justify-content: center;
    align-items: center;

    .input {
        width: 500px;
    }
}
</style>
  