<template>
  <div class="p-6">
    <h2 class="text-2xl font-bold mb-4">Your Tasks</h2>

    <!-- Task Creation Form -->
    <form @submit.prevent="handleSubmit" class="mb-6 grid gap-2 max-w-md">
      <input
        v-model="form.title"
        placeholder="Task Title"
        required
        class="p-2 border rounded"
      />
      <textarea
        v-model="form.description"
        placeholder="Description"
        class="p-2 border rounded"
      />
      <input
        v-model="form.effort_days"
        type="number"
        placeholder="Effort (Days)"
        class="p-2 border rounded"
      />
      <input v-model="form.due_date" type="date" class="p-2 border rounded" />
      <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded">
        {{ form.id ? "Update Task" : "Create Task" }}
      </button>
    </form>

    <!-- Export Button -->
    <button
      @click="exportToExcel"
      class="bg-green-500 text-white px-4 py-2 rounded mb-4"
    >
      Export to Excel
    </button>

    <!-- Task List -->
    <div v-if="tasks.length" class="space-y-4">
      <div
        v-for="task in tasks"
        :key="task.id"
        class="p-4 border rounded shadow"
      >
        <h3 class="text-lg font-semibold">{{ task.title }}</h3>
        <p>{{ task.description }}</p>
        <p>Effort: {{ task.effort_days }} day(s)</p>
        <p>Due: {{ task.due_date }}</p>
        <div class="mt-2">
          <button @click="editTask(task)" class="text-blue-500 mr-2">
            Edit
          </button>
          <button @click="deleteTask(task.id)" class="text-red-500">
            Delete
          </button>
        </div>
      </div>
    </div>

    <p v-else>No tasks found.</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      tasks: [],
      form: {
        id: null,
        title: "",
        description: "",
        effort_days: "",
        due_date: "",
      },
    };
  },
  methods: {
    async fetchTasks() {
      try {
        const res = await axios.get(
          "http://localhost:8000/api/tasks/",
          this.authHeader()
        );
        this.tasks = res.data;
        console.log(this.tasks);
      } catch (err) {
        console.error("Failed to fetch tasks", err);
      }
    },
    async handleSubmit() {
      try {
        if (this.form.id) {
          await axios.put(
            `http://localhost:8000/api/tasks/${this.form.id}/`,
            this.form,
            this.authHeader()
          );
        } else {
          await axios.post(
            "http://localhost:8000/api/tasks/",
            this.form,
            this.authHeader()
          );
        }
        this.resetForm();
        this.fetchTasks();
      } catch (err) {
        console.error("Error submitting task:", err);
      }
    },
    async deleteTask(id) {
      try {
        await axios.delete(
          `http://localhost:8000/api/tasks/${id}/`,
          this.authHeader()
        );
        this.fetchTasks();
      } catch (err) {
        console.error("Error deleting task:", err);
      }
    },
    editTask(task) {
      this.form = { ...task };
    },
    resetForm() {
      this.form = {
        id: null,
        title: "",
        description: "",
        effort: "",
        due_date: "",
      };
    },
    async exportToExcel() {
      try {
        const res = await axios.get("http://localhost:8000/api/tasks/export/", {
          ...this.authHeader(),
          responseType: "blob",
        });

        const url = window.URL.createObjectURL(new Blob([res.data]));
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", "tasks.xlsx");
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      } catch (err) {
        console.error("Failed to export tasks:", err);
      }
    },
    authHeader() {
      const token = localStorage.getItem("token");
      return {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      };
    },
  },
  mounted() {
    this.fetchTasks();
  },
};
</script>

<style scoped>
input,
textarea {
  width: 100%;
}
</style>
