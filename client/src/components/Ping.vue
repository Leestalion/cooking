<template>
    <div>
        <p>{{ msg }}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://0.0.0.0:5000/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          if (!error.response) {
              // network error
              this.errorStatus = 'Error: Network Error';
          } else {
              this.errorStatus = error.response.data.message;
          }
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
