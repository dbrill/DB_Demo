<template>
  <div>
    <h1 class="header"> My Shopping List! </h1>
    <list-row v-for="item in items" class="list-row"
      :key="item.item"
      :listItem="item"/>
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
import { ListItem } from '../util/listItem';
import ListRow from '../components/ListRow.vue';
// Define the component in class-style
@Options({
  components: {
    ListRow
  }
})
export default class ShoppingList extends Vue {

  items: ListItem[] = [{
    item: 'eggs',
    quantity: 1,
    price: 2.99
  },
  {
    item: 'milk',
    quantity: 2,
    price: 3.99
  }];

  protected get totalCost(): number {
    let sum = 0;
    this.items.forEach((item: ListItem) => {
      sum += item.price * item.quantity;
    });

    return sum;
  }
}
</script>
<style lang="scss" scoped>
.total {
  color: rgb(60, 165, 60);
}
</style>