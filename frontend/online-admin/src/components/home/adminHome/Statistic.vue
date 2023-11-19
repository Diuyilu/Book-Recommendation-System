<template>
  <el-row :gutter="16">
    <el-col :span="3">
      <div class="statistic-card">
        <el-statistic :value="774320">
          <template #title>
            <div style="display: inline-flex; align-items: center ;font-size: 18px" >
              图书总数
              <el-tooltip
                  effect="dark"
                  content="本系统可检索的图书数量"
                  placement="top"
              >
                <el-icon style="margin-left: 4px" :size="12">
                  <Warning />
                </el-icon>
              </el-tooltip>
            </div>
          </template>
        </el-statistic>
      </div>
    </el-col>
    <el-col :span=5>
      <div class="statistic-card">
        <el-statistic :value="645332">
          <template #title>
            <div style="display: inline-flex; align-items: center;font-size: 18px">
              图书馆藏书数
              <el-tooltip
                  effect="dark"
                  content="校图书馆可借阅图书数量"
                  placement="top"
              >
                <el-icon style="margin-left: 4px" :size="12">
                  <Warning />
                </el-icon>
              </el-tooltip>
            </div>
          </template>
        </el-statistic>
        <div class="statistic-footer">
          <div class="footer-item">
            <span>图书占比</span>
            <span class="green">
              78%
            </span>
          </div>
        </div>
      </div>
    </el-col>
    <el-col :span="3">
      <div class="statistic-card">
        <el-statistic :value="2332">
          <template #title>
            <div style="display: inline-flex; align-items: center ;font-size: 18px">
              用户数
              <el-tooltip
                  effect="dark"
                  content="在校学生总数"
                  placement="top"
              >
                <el-icon style="margin-left: 4px" :size="12">
                  <Warning />
                </el-icon>
              </el-tooltip>
            </div>
          </template>
        </el-statistic>
      </div>
    </el-col>
    <el-col :span="5">
      <div class="statistic-card">
        <el-statistic :value="765">
          <template #title>
            <div style="display: inline-flex; align-items: center ;font-size: 18px">
              读者数
              <el-tooltip
                  effect="dark"
                  content="有过借阅行为的学生数量"
                  placement="top"
              >
                <el-icon style="margin-left: 4px" :size="12">
                  <Warning />
                </el-icon>
              </el-tooltip>
            </div>
          </template>
        </el-statistic>
        <div class="statistic-footer">
          <div class="footer-item">
            <span>用户借阅率</span>
            <span class="red">
              34%
            </span>
          </div>
        </div>
      </div>
    </el-col>
    <el-col :span="4">
      <div class="statistic-card">
        <el-statistic :value="284454">
          <template #title>
            <div style="display: inline-flex; align-items: center;font-size: 18px">
              图书借阅总次数
              <el-tooltip
                  effect="dark"
                  content='图书借阅记录数总和'
                  placement="top"
              >
                <el-icon style="margin-left: 4px" :size="12">
                  <Warning />
                </el-icon>
              </el-tooltip>
            </div>
          </template>
        </el-statistic>
      </div>
    </el-col>
    <el-col :span="3">
      <div class="statistic-card">
        <el-statistic :value="4376">
          <template #title>
            <div style="display: inline-flex; align-items: center;font-size: 18px">
              被借阅图书数
              <el-tooltip
                  effect="dark"
                  content="有过借阅记录的图书数"
                  placement="top"
              >
                <el-icon style="margin-left: 4px" :size="12">
                  <Warning />
                </el-icon>
              </el-tooltip>
            </div>
          </template>
        </el-statistic>
        <div class="statistic-footer">
          <div class="footer-item">
            <span>图书借阅率</span>
            <span class="red">
              12%
            </span>
          </div>
        </div>
      </div>
    </el-col>
  </el-row>
</template>

<script lang="ts" setup>
import {
  ArrowRight,
  CaretBottom,
  CaretTop,
  Warning,
} from '@element-plus/icons-vue'
</script>

<style scoped>
:global(h2#card-usage ~ .example .example-showcase) {
  background-color: var(--el-fill-color) !important;
}

.el-statistic {
  --el-statistic-content-font-size: 28px;
}

.statistic-card {
  height: 100%;
  padding: 20px;
  border-radius: 4px;
  background-color: var(--el-bg-color-overlay);
}

.statistic-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  font-size: 12px;
  color: var(--el-text-color-regular);
  margin-top: 16px;
}

.statistic-footer .footer-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.statistic-footer .footer-item span:last-child {
  display: inline-flex;
  align-items: center;
  margin-left: 4px;
}

.green {
  color: var(--el-color-success);
}
.red {
  color: var(--el-color-error);
}
</style>
