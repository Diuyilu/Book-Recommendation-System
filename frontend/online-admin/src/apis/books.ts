import { get, post } from './api'

export const getBookInfoAPI = (data) => get('/teacher_portrait/get_book_info', data)

// 书籍数据结构
export interface BookData {
  db_id: string
  book_title: string
  author: string
  press: string
  content_validity: string
  publication_year: string
}
