<template>
  <ul v-if="categories" class="categories">
    <CategoryItem
        v-for="category in categories"
        v-bind:category="category"
    />
  </ul>
  <div v-else class="categories_unauth">
    <p class="categories_unauth-text">Просмотр категорий доступен только авторизованным пользователям</p>
  </div>
</template>

<script>
import CategoryItem from "./CategoryItem";

export default {
  name: 'CategoryList',
  components: {
    CategoryItem
  },
  props: ["categories"],
}
</script>

<style scoped lang="scss">

</style>
