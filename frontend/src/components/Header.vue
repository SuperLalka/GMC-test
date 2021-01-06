<template>
  <header class="header">
    <h1 class="header__title">Library</h1>
    <Authorization />
  </header>
</template>

<script>
import Authorization from "./Authorization";

export default {
  name: 'Header',
  components: {
    Authorization
  },
}
</script>

<style scoped lang="scss">
header {
  align-items: center;
  display: flex;
  justify-content: center;
  background-color: #2c3e50;
  background-image: url(//img4.goodfon.ru/wallpaper/nbig/5/16/biblioteka-knigi-fon.jpg);
  background-repeat: no-repeat;
  background-size: cover;
  border-bottom: 3px solid black;
  min-height: 20vh;
}

.header__title {
  background: black;
  border: 1px solid white;
  color: white;
  font-size: 70px;
  margin: 0;
  padding: 20px;
}
</style>
