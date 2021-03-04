<template>
  <div class="list-container">
    <div class="item">
        {{ listItem.item }} ({{ listItem.quantity }})
    </div>
    <div class="price">
        ${{ listItem.price }}
    </div>
  </div>
</template>

<script lang="ts">
import { Vue } from 'vue-class-component';
import { Prop } from 'vue-property-decorator';
import { ListItem } from '../util/listItem';

export default class ListRow extends Vue {
  
  @Prop({ required: true, default: {}})
  listItem: ListItem;
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
}
</style>