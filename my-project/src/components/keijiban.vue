<template>
  <div class="keijiban">
    <b>
      <label class="m-1" for="title">ニックネームとメッセージを入力して投稿ボタンを押してください</label>
    </b>
    <hr />
    <b-form-input class="w-25 m-1" v-model="name" placeholder="ニックネーム"></b-form-input>
    <div class="w-50 p-3 mb-1 text-light">
      <b-form-textarea
        class="m-1"
        id="textarea"
        v-model="message"
        placeholder="メッセージ"
        rows="3"
        max-rows="6"
      ></b-form-textarea>
    </div>
    <b-button
      class="m-1"
      type="submit"
      size="lg"
      variant="outline-primary"
      v-on:click="postkeijiban"
    >投稿</b-button>
    <hr />
    <div class="text-center" v-show="spinnerFlag">
      <b-spinner variant="primary" label="Spinning"></b-spinner>
    </div>

    <ul v-for="item in sortedItemsByPostid" v-bind:key="item.POST_ID">
      <b-card class="m-1 w-50">
        <li class="m-1" style="list-style: none;">
          <p class="m-1">投稿ID：{{item.POST_ID}}</p>
          <p class="m-1">名前：{{item.POST_NAME}}投稿日時：{{item.CRT_TIMESTAMP}}</p>
          <p class="m-1">{{item.POST_MESSAGE}}</p>
        </li>
      </b-card>
    </ul>
  </div>
</template>

<script>
export default {
  name: "keijiban",
  data() {
    return {
      name: "",
      message: "",
      results: [],
      spinnerFlag: false
    };
  },
  created() {
    this.getkeijiban();
  },
  methods: {
    demo() {
      alert("test");
    },
    getkeijiban() {
      this.spinnerFlag = !this.spinnerFlag;

      this.axios
        .get(
          "https://onzmaql4xa.execute-api.ap-northeast-1.amazonaws.com/DEV",
          {
            headers: {
              "X-API-KEY": "H1uVk1aKo2e9EjPmdoFo1j3gUCaMfxRaadGzYhw5"
            }
          }
        )
        .then(response => {
          this.spinnerFlag = !this.spinnerFlag;
          this.results = response.data;
          console.log(response.data);
        })
        .catch(e => {
          this.spinnerFlag = !this.spinnerFlag;
          console.log(e);
        });
    },
    postkeijiban() {
      this.axios
        .post(
          "https://1o9708g3dl.execute-api.ap-northeast-1.amazonaws.com/DEV",
          {
            POST_NAME: this.name,
            POST_MESSAGE: this.message
          },
          {
            headers: {
              "X-API-KEY": "H1uVk1aKo2e9EjPmdoFo1j3gUCaMfxRaadGzYhw5"
            }
          }
        )
        .then(response => {
          alert("メッセージを投稿しました");
          console.log(response.data);
          this.getkeijiban();
        })
        .catch(e => {
          alert("メッセージの投稿に失敗しました");
          console.log(e);
        });
    }
  },
  computed: {
    sortedItemsByPostid() {
      return this.results.sort((a, b) => {
        return a.POST_ID < b.POST_ID ? 1 : a.POST_ID > b.POST_ID ? -1 : 0;
      });
    }
  }
};
</script>

<style>
</style>