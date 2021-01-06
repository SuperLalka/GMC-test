<template>
  <ul v-if="is_Authorize" class="categories">
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
  data() {
    return {
      categories: null,
    }
  },
  computed: {
    is_Authorize() {
      return this.$store.state.is_Authorize
    }
  },
  created() {
    fetch("http://localhost:8000/api/categories/", {
      method: 'GET',
      headers: {
        'Authorization': "JWT" + " " + localStorage.getItem('user_token'),
      }
    })
        .then(response => {
          return response.ok
              ? response.json()
              : false
        })
        .then(data => {
          this.categories = data;
        })
  }
}
</script>

<style scoped lang="scss">
.categories {
  margin: 0;
  padding: 10px;
}
</style>
