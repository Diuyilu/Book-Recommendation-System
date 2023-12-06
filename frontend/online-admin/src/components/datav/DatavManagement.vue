<template>
  <div class="iframe-container">
    <iframe :src="url" id="main" name="main" class="twodw" frameborder="0" scrolling="no"></iframe>
  </div>
</template>

<script setup lang="ts">
// import { createHmac } from 'crypto'
// import CryptoJS from 'crypto-js'
import CryptoJS from 'crypto-js/crypto-js'

var token = 'KH9Yzpjz6uxNTkE0AzgSSDcDyU9gPdC5'
var screenID = '7dbddfb1ecbaeede70ed496dd6573c83'
var time = Date.now()
var stringToSign = screenID + '|' + time
var signature = CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(stringToSign, token))
var url =
  'http://datav.aliyun.com/share/' +
  screenID +
  '?_datav_time=' +
  time +
  '&_datav_signature=' +
  encodeURIComponent(signature)
</script>

<style lang="scss" scoped>
.iframe-container {
  background-color: #050a10;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
#main {
  width: calc(100vw - 320px);
  min-height: calc(100vh - 115px);
}
</style>
