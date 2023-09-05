<template>
  <div id="login">
    <div class="login-box">
      <div class="logo">
        <el-image
          src="https://www.cuc.edu.cn/_upload/article/images/2d/8f/0d01cab040ba9acf65ff3b0a2910/b2a81a00-4154-4480-bc1b-9f2b2f0184e4.jpg"
          fit="fill" :lazy="true"></el-image>
      </div>
      <el-form>
        <el-form-item>
          <el-input class="input" placeholder="用户名" :prefix-icon="User" />
        </el-form-item>
        <el-form-item>
          <el-input class="input" placeholder="密码" :prefix-icon="Lock" />
        </el-form-item>
        <div class="btns">
          <el-button type="primary" class="btn">登录</el-button>
          <div class="btn reset">重置</div>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { User, Lock } from '@element-plus/icons-vue';
</script>

<style lang="scss" scoped>
#login {
  height: 100vh;
  background: linear-gradient(to right, #2b2c43, #1e3158);
  display: flex;
  justify-content: center;
  align-items: center;

  .login-box {
    width: 360px;
    height: 450px;
    background-color: #fff;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;

    .logo {
      width: 120px;
      height: 120px;
      border-radius: 50%;
      box-shadow: 0 0 4px 2px #9fa1a5;
      margin-bottom: 30px;
      overflow: hidden;
    }

    .el-form {
      width: 90%;
      margin-top: 30px;

      .input {
        height: 40px;

        // 样式穿透
        :deep(.el-input__wrapper) {
          border-radius: 20px;
          border: 1px solid #000;
        }
      }

      .btns {
        display: flex;
        // 横向排列
        // justify-content: center;
        // 竖向排列
        flex-direction: column;
        align-items: center;

        .btn {
          width: 100%;
          height: 40px;
          border-radius: 20px;
          margin-bottom: 20px;
          cursor: pointer;
        }

        .reset {
          text-align: center;
        }
      }
    }
  }


}
</style>