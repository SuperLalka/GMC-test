<template>
  <main class="main">
    <Aside
        v-bind:categories="categories"
    />
    <Section/>
  </main>
</template>

<script>
import Aside from "./Aside";
import Section from "./Section";

export default {
  name: 'Main',
  components: {
    Aside, Section
  },
  data() {
    return {
      categories: {},
    }
  },
  mounted() {
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
main {
  display: flex;
  min-height: calc(100vh - (20vh + 150px));
}
</style>
