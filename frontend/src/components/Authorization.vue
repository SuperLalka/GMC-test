<template>
  <div class="auth-block">
    <form v-if="!is_Authorize" class="auth-block__form" @submit.prevent="Authentication">
      <input type="text" v-model="username" required placeholder="Login">
      <input type="password" v-model="password" required placeholder="Password">
      <button type="submit">Войти</button>
    </form>
    <div v-else class="auth-block__unauth">
      <button class="unauth-button" v-on:click.prevent="UnAuthentication">Разлогиниться</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      is_Authorize: !!localStorage.getItem('user_token'),
      username: "",
      password: ""
    }
  },
  methods: {
    Authentication() {
      const requestOptions = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({username: this.username, password: this.password})
      };
      fetch('http://localhost:8000/token/', requestOptions)
          .then(response => response.json())
          .then(data => {
            data.access
                ? localStorage.setItem('user_token', data['access'])
                : alert('Incorrect login or password')
          })
    },
    UnAuthentication() {
      localStorage.removeItem('user_token');
    }
  },
}
</script>

<style scoped lang="scss">
.auth-block {
  background-color: #fdfffc70;
  border-bottom-left-radius: 25px;
  height: 100px;
  position: absolute;
  right: 0;
  top: 0;
  width: 300px;
}

.auth-block__form,
.auth-block__unauth {
  align-items: center;
  display: flex;
  flex-flow: column;
  justify-content: center;
  height: 100%;
}

.unauth-button {
  font-size: 20px;
  height: 40%;
}
</style>
