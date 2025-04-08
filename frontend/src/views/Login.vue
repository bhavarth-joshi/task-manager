<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="username" required />
      <input
        type="password"
        v-model="password"
        placeholder="Password"
        required
      />
      <button type="submit">Login</button>
    </form>
    <p>{{ error }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      password: "",
      error: "",
    };
  },
  methods: {
    async login() {
      try {
        const res = await axios.post("http://localhost:5000/api/auth/login", {
          username: this.username,
          password: this.password,
        });

        localStorage.setItem("token", res.data.token);
        this.$router.push("/tasks");
      } catch (err) {
        this.error = "Login failed";
        console.error(err);
      }
    },
  },
};
</script>
