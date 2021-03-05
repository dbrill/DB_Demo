<template>
  <div class="list-container">
    <div class="item">
        {{ listItem.item }} ({{ listItem.quantity }})
    </div>
    <div class="priceAndRemove">
      <div class="price">
          ${{ listItem.price }}
      </div>
      <div class="remove" @click="remove">
        X
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Options } from 'vue-class-component';
import { Prop } from 'vue-property-decorator';
import { ListItem } from '../util/listItem';

@Options({
  emits: ['remove']
})
export default class ListRow extends Vue {
  
  @Prop({ required: true, default: {}})
  listItem: ListItem;

  protected remove() {
    this.$emit('remove');
  }
}
</script>
<style lang="scss" scoped>
.list-container {
  border: 2px solid #415451;
  border-radius: 12px;
  display: flex;
  flex-direction: row;
  font-size: 30px;
  justify-content: space-around;
  margin-left: 250px;
  margin-right: 250px;
  margin-bottom: 15px;

  &:hover {
    border: 2px solid #8ffae9;
  }

  .item {
    width: 200px;
  }
  .priceAndRemove {
    display: flex;
    flex-direction: row;
    width: 200px;
    justify-content: space-around;
    align-items: center;

    .remove {
      &:hover {
        color: red;
        cursor: pointer;
      }
    }
  }
}
</style>