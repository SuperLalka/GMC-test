<template>
  <aside class="aside">
    <CategoryList
      v-bind:categories="categories"
    />
  </aside>
</template>

<script>
import CategoryList from "../components/CategoryList";

export default {
  name: 'Aside',
  components: {
    CategoryList
  },
  props:["categories"],
}
</script>

<style scoped lang="scss">
aside {
  background-color: aliceblue;
  border-right: 1px solid darkblue;
  flex: 1;
}
</style>
