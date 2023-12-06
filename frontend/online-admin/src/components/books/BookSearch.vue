<template>
  <router-view></router-view>
  <div v-show="flag">
    <div id="search">
      <el-form :inline="true" :model="form" @submit.prevent>
        <el-form-item prop="value">
          <el-input
            class="input"
            v-model="form.value"
            placeholder="请输入书名、作者等书籍信息"
            @keydown.enter="keyDown()"
          />
        </el-form-item>
        <el-form-item prop="button">
          <el-button type="primary" class="btn" @click="search_book_info">搜索</el-button>
        </el-form-item>
      </el-form>
    </div>
    <!-- <el-table :data="tableData" style="width: 100%"> -->
    <el-table
      :data="tableData()"
      style="width: 100%; cursor: pointer"
      @row-click="push_router"
      v-show="tableData().length > 0"
    >
      <el-table-column prop="book_title" label="书籍名称"></el-table-column>
      <el-table-column label="书籍封面">
        <template #default="scope">
          <div style="display: flex; align-items: center" v-if="scope.row.image_address">
            <el-image :src="scope.row.image_address" style="height: 100px" />
          </div>
          <div class="image_title" v-else>
            {{ scope.row.book_title }}
          </div>
        </template>
      </el-table-column>
      <el-table-column prop="author" label="作者"></el-table-column>
      <el-table-column prop="press" label="出版社"></el-table-column>
      <el-table-column prop="label" label="书籍类型"></el-table-column>
    </el-table>
    <div class="pagination-block" v-show="tableData().length > 0">
      <!-- <div class="example-demonstration">分页</div> -->
      <el-pagination
        background
        :page-sizes="[5, 10]"
        :page-size="5"
        layout="prev, pager, next"
        :total="state.total"
        @current-change="handleCurrentChange"
        @size-change="handleSizeChange"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, defineComponent, reactive, toRefs, watch, onMounted, onUnmounted } from 'vue'
import { getBookInfoAPI, searchBookInfoAPI } from '@/apis/books'
import { useRouter } from 'vue-router'

const router = useRouter()

let flag = true

function push_router(row, column, event) {
  const book_id = row.book_id
  console.log(book_id)
  router.push({
    name: 'booksearchinfo',
    query: {
      book_id: JSON.stringify(book_id)
    }
  })
}

// 使用watch监听路由，让flag发声变化，当路由变为booksearchinfo时，flag变为false，此时不显示搜索框。当路由变为booksearch时，flag变为true，此时显示搜索框
watch(
  () => router.currentRoute.value.name,
  (to, from) => {
    if (to === 'booksearchinfo') {
      change_flag(false)
    } else if (to === 'booksearch') {
      change_flag(true)
    }
  }
)

function change_flag(x) {
  flag = x
}

interface Form {
  value: string
}
const form = ref<Form>({
  value: ''
})

const message = ref()

const get_book_info = async () => {
  const res = await getBookInfoAPI()
  console.log(res.book_list)
  message.value = res.book_list
  state.total = res.book_list.length
}
const state = reactive({
  page: 1,
  limit: 5,
  //   total: message.value.length
  total: 0
})

const search_book_info = async () => {
  const res = await searchBookInfoAPI(form.value)
  console.log(res.book_list)
  message.value = res.book_list
  state.total = res.book_list.length
}

//点击回车键登录
const keyDown = (e?) => {
  if (e.keyCode == 13 || e.keyCode == 100) {
    search_book_info()
  }
}
onMounted(() => {
  //绑定监听事件
  window.addEventListener('keydown', keyDown)
})

onUnmounted(() => {
  //销毁事件
  window.removeEventListener('keydown', keyDown, false)
})
//表格用到的参数

//前端限制分页（tableData为当前展示页表格）
const tableData = () => {
  if (message.value) {
    return message.value.filter(
      (item, index) => index < state.page * state.limit && index >= state.limit * (state.page - 1)
    )
  } else return []
}

const handleCurrentChange = (e) => {
  state.page = e
}
//改变页数限制
const handleSizeChange = (e) => {
  state.limit = e
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
.pagination-block {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.image_title {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  width: 80px;
  height: 100px;
  background-color: #e7e5e5;
  font-size: 10px;
  font-weight: 600;
  color: #29455b;
  text-align: center;
}
</style>
