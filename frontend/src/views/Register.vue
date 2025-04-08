<template>
  <div class="p-6 max-w-md mx-auto">
    <h2 class="text-2xl font-bold mb-4">Register</h2>
    <form @submit.prevent="register" class="grid gap-3">
      <input
        v-model="username"
        placeholder="username"
        required
        class="p-2 border rounded"
      />
      <input
        v-model="password"
        type="password"
        placeholder="Password"
        required
        class="p-2 border rounded"
      />
      <button type="submit" class="bg-green-500 text-white px-4 py-2 rounded">
        Register
      </button>
    </form>
    <p class="text-red-500 mt-2">{{ error }}</p>
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
    async register() {
      try {
        const res = await axios.post(
          "http://localhost:5000/api/auth/register",
          {
            username: this.username,
            password: this.password,
          }
        );

        // Save token and redirect
        // localStorage.setItem("token", res.data.token);
        this.$router.push("/");
      } catch (err) {
        this.error = "Registration failed";
        console.error(err);
      }
    },
  },
};
</script>
