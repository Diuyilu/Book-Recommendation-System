<template>
  <RouterView> </RouterView>
  <div v-show="flag">
    <div>
      <el-row>
        <el-col :span="24">
          <div style="font-size: 20px">您的收藏</div>
          <el-row class="book_list" :gutter="40">
            <el-col :span="4" v-for="book in tableData()" :key="book.book_id" style="margin-bottom: 20px">
              <el-card class="box-card" shadow="hover" style="height: 280px; width: 200px; border: 0px; cursor: pointer"
                @click="push_router(book.book_id)">
                <div v-if="book.image_address">
                  <img :src="book.image_address" style="width: 155px" id="image" />
                </div>
                <div v-else id="image_title">
                  <div style="text-align: center; font-weight: 500">
                    {{ book.book_title }}
                  </div>
                </div>
              </el-card>
              <div class="book_title">
                {{ book.book_title.length > 15 ? book.book_title.slice(0, 15) + '...' : book.book_title }}
              </div>
              <div class="utils">
                <div class="dislike">
                  <el-tooltip content="取消收藏" placement="top">
                    <el-icon @click="delet_book_info_by_collection(book.book_id)"
                      style="cursor: pointer;margin-right: 25px;" :size="30">
                      <CircleClose />
                    </el-icon>
                  </el-tooltip>
                </div>
                <div class="hasread">
                  <el-tooltip content="已经看过" placement="top">
                    <el-icon @click="push_borrowing_by_recommend(book.TSBH, book.book_title)"
                      style="cursor: pointer;margin-right: 25px;" :size="30">
                      <View />
                    </el-icon>
                  </el-tooltip>

                </div>
              </div>
            </el-col>
          </el-row>
        </el-col>
        <div class="pagination-block">
          <!-- <div class="example-demonstration">分页</div> -->
          <el-pagination background :page-sizes="[6, 10]" :page-size="6" layout="prev, pager, next" :total="state.total"
            @current-change="handleCurrentChange" @size-change="handleSizeChange" />
        </div>
      </el-row>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { onMounted, watch, reactive, ref } from 'vue'
import { getBookInfoByCollectionAPI, getBookInfoAPI, deleteBookInfoByCollectionAPI, pushBorrowingByRecommendAPI } from '@/apis/books'
import { getUserinfoApi } from '@/apis/userinfo'
import { ElMessage } from 'element-plus'

const books = ref()

const fakerating = ref(Array.from({ length: 100 }, () => (Math.random() * 4 + 5).toFixed(1)));

let flag = true
const message = ref()

const get_user_info = async () => {
  const res = await getUserinfoApi()
  console.log(res.user_list[0].username)
  return res.user_list[0].username
}

const get_book_info_by_collection = async () => {
  const username = await get_user_info()
  const params = { username: username }
  const res = await getBookInfoByCollectionAPI(params)
  console.log(res.book_list)
  books.value = res.book_list
  message.value = res.book_list
  state.total = res.book_list.length
}

const delet_book_info_by_collection = async (book_id) => {
  const username = await get_user_info()
  const params = { username: username, book_id: book_id }
  const res = await deleteBookInfoByCollectionAPI(params)
  console.log(res)
  console.log(res.message)
  if (res.status === 1) {
    ElMessage.success(res.message)
  } else {
    ElMessage.error(res.message)
  }
  get_book_info_by_collection()
}

const push_borrowing_by_recommend = async (book_id, book_name) => {
  const username = await get_user_info()
  const params = { username: username, book_id: book_id, book_name: book_name }
  const res = await pushBorrowingByRecommendAPI(params)
  console.log(res)
  console.log(res.message)
  if (res.status === 1) {
    ElMessage.success(res.message)
  } else {
    ElMessage.error(res.message)
  }
}


// const get_book_info = async () => {
//   const res = await getBookInfoAPI()
//   console.log(res.book_list)
//   books.value = res.book_list
//   state.total = res.book_list.length
//   message.value = res.book_list
// }


const tableData = () => {
  if (message.value) {
    return message.value.filter(
      (item, index) => index < state.page * state.limit && index >= state.limit * (state.page - 1)
    )
  } else return []
}

const router = useRouter()
function push_router(db_id) {
  const book_id = db_id
  console.log(book_id)
  router.push({
    name: 'collectioninfo',
    query: {
      book_id: JSON.stringify(book_id)
    }
  })
}

function change_flag(x) {
  flag = x
}

watch(
  () => router.currentRoute.value.name,
  (to, from) => {
    if (to === 'collectioninfo') {
      change_flag(false)
    } else if (to === 'collection') {
      change_flag(true)
    }
  }
)

const state = reactive({
  page: 1,
  limit: 6,
  // total: message.value.length
  total: 0
})

const handleCurrentChange = (e) => {
  state.page = e
}
//改变页数限制
const handleSizeChange = (e) => {
  state.limit = e
}

onMounted(() => {
  console.log('yesyesyes!')
  get_book_info_by_collection()
})


</script>

<style lang="scss" scoped>
.book_list {
  margin-top: 20px;
  display: flex;
  // justify-content: center;
  // align-items: center;
  height: 390px;
}

.box-card {
  display: flex;
  justify-content: center;
  align-items: center;
}

.book_title {
  margin-top: 10px;
  margin-right: 40px;
  display: flex;
  justify-content: center;
  // align-items: center;
  text-align: center;
  height: 50px;
}

.pagination-block {
  margin-top: 40px;
  margin-left: 34vw;
  // justify-content: center;
  // align-items: center;
}

#image_title {
  display: flex;
  justify-content: center;
  /* 水平居中 */
  align-items: center;
  /* 垂直居中 */
  width: 155px;
  height: 200px;
  background-color: #e7e5e5;
  font-size: 20px;
  font-weight: 600;
  color: #29455b;
}

#interest_sectl {
  display: flex;
  justify-content: center;
  /* 水平居中 */
  align-items: center;
  /* 垂直居中 */
  margin-right: 75px;
  height: 60px;
}

.utils {
  display: flex;
  justify-content: center;
  margin-right: 10px;
}

.rating_num {
  // 字体设置为粗体
  font-weight: bold;
}
</style>
