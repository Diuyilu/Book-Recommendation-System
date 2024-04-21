import { FormRules } from 'element-plus'

export const rules: FormRules = {
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
    { min: 3, max: 40, message: '长度3-40字符', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 3, max: 40, message: '长度3-40字符', trigger: 'blur' }
  ]
}
