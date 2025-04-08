<template>
  <div>
    <!-- Navbar -->
    <nav class="bg-gray-800 text-white p-4 flex justify-between items-center">
      <div class="font-bold text-lg">📝 Task Manager</div>
      <div class="space-x-4">
        <router-link to="/tasks" class="hover:underline">Tasks</router-link>
        <router-link v-if="!isLoggedIn" to="/login" class="hover:underline"
          >Login</router-link
        >
        <router-link v-if="!isLoggedIn" to="/register" class="hover:underline"
          >Register</router-link
        >
        <button
          v-if="isLoggedIn"
          @click="logout"
          class="hover:underline text-red-300"
        >
          Logout
        </button>
      </div>
    </nav>

    <!-- Page Content -->
    <router-view class="mt-6" />
  </div>
</template>

<script>
export default {
  computed: {
    isLoggedIn() {
      return !!localStorage.getItem("token");
    },
  },
  methods: {
    logout() {
      localStorage.removeItem("token");
      this.$router.push("/login");
    },
  },
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
}
</style>
