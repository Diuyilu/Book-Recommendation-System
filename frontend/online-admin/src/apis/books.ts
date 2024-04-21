import { get, post } from './api'

// export const getBookInfoAPI = (data) => get('/teacher_portrait/get_book_info', data)
export const getBookInfoAPI = () => get('/api/api/get_book_info')
export const searchBookInfoAPI = (data) => post('/api/api/search_book_info', data)
export const getBookInfoByIdAPI = (data) => post('/api/api/get_book_info_by_id', data)
export const getNewBookInfoAPI = () => get('/api/api/get_new_book_info')
export const getPopBookInfoAPI = () => get('/api/api/get_pop_book_info')
export const getBookLabelAPI = () => get('/api/api/get_book_label')
export const getBookByLabelAPI = (data) => post('/api/api/get_book_by_label', data)
export const getBookInfoByBorrowingAPI = (data) => post('/api/api/get_book_info_by_borrowing', data)
export const getBookInfoByCollectionAPI = (data) =>
  post('/api/api/get_book_info_by_collection', data)
export const pushBookInfoByRecommendAPI = (data) =>
  post('/api/api/push_book_info_by_recommend', data)
export const deleteBookInfoByCollectionAPI = (data) =>
  post('/api/api/delete_book_info_by_collection', data)
export const pushBorrowingByRecommendAPI = (data) =>
  post('/api/api/push_borrowing_by_recommend', data)
export const getUserBookInfoAPI = (data) => post('/api/api/get_user_book_info', data)
export const deleteBookInfoByRecommendAPI = (data) =>
  post('/api/api/delete_book_info_by_recommend', data)
export const judgeCollectionAPI = (data) => post('/api/api/judge_collection', data)

// 书籍数据结构
export interface BookData {
  db_id: string
  book_title: string
  author: string
  press: string
  content_validity: string
  publication_year: string
}
