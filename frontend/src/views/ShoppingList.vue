<template>
  <div>
    <h1 class="header"> My Shopping List! </h1>
    <list-row v-for="item in items" class="list-row"
      :key="item.item"
      :listItem="item"
      @remove="() => remove(item)"/>
    <add-item @add="add"/>
    <div class="separator">
      --------------------------------
    </div>
    <h1 class="total">
      Total: ${{ totalCost }}
    </h1>
  </div>
</template>

<script lang="ts">
import { Vue, Options } from 'vue-class-component';
import axios from 'axios';

import { ListItem } from '../util/listItem';
import ListRow from '../components/ListRow.vue';
import AddItem from '../components/AddItem.vue';

// Define the component in class-style
@Options({
  components: {
    ListRow,
    AddItem
  }
})
export default class ShoppingList extends Vue {

  items: ListItem[] = [];

  mounted() {
    this.populateData()
  }

  protected get totalCost(): number {
    let sum = 0;
    this.items.forEach((item: ListItem) => {
      sum += item.price * item.quantity;
    });

    return Math.ceil(sum * 100) / 100;
  }

  async populateData() {
    const res = await axios.get('http://localhost:5000/list');
    this.items = res.data;
  }
  remove(itemToRemove: ListItem) {
    this.items = this.items.filter((item) => item !== itemToRemove);
    axios.delete(`http://localhost:5000/${itemToRemove.id}`)
  }

  async add(itemToAdd: ListItem) {
    await axios.post('http://localhost:5000/item', itemToAdd)
    this.populateData()
  }
}
</script>
<style lang="scss" scoped>
.total {
  color: rgb(60, 165, 60);
}

.separator {
  margin-top: 25px;
}
</style>