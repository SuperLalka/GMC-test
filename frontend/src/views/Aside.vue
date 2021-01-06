<template>
  <aside class="aside">
    <CategoryList />
  </aside>
</template>

<script>
import CategoryList from "../components/CategoryList";

export default {
  name: 'Aside',
  components: {
    CategoryList
  },
}
</script>

<style scoped lang="scss">
aside {
  background-color: aliceblue;
  border-right: 1px solid darkblue;
  flex: 1;
}
</style>
