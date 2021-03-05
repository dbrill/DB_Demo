<template>
<div class="add-item-container">
  <div class="input-container">
      <input v-model="item" class="input item-input" placeholder="item name"
					:class="{'empty': nullItem}"/>
      <input v-model="quantity" class="input quantity-input" placeholder="quantity"
					:class="{'empty': nullQuantity}"/>
      <input v-model="price" class="input price-input" placeholder="price"
					:class="{'empty': nullPrice}"/>
  </div>
  <button class="submit" @click="addItem" :class="{'disabled': !submittable}">
      Add Item
  </button>
</div>
</template>

<script lang="ts">
import { Vue, Options } from 'vue-class-component';

@Options({
  emits: ['add']
})
export default class ListRow extends Vue {
 
  item = '';
  price = null;
  quantity = null;


	protected get submittable() {
		return !this.nullItem && !this.nullPrice &&!this.nullQuantity;
	}

	protected get nullItem() {
		return this.isNullOrWhiteSpace(this.item);
	}

	protected get nullPrice() {
		return this.isNullOrWhiteSpace(this.price);
	}

	protected get nullQuantity() {
		return this.isNullOrWhiteSpace(this.quantity);
	}

	private isNullOrWhiteSpace(thing: any): boolean {
		return thing == null || thing === '';
	}

  addItem() {
		if (!this.submittable) {
			return;
		}
		this.$emit('add', {
			item: this.item,
			quantity: this.quantity,
			price: this.price
		});
		this.reset();
  }

	reset() {
		this.item = '';
		this.quantity = null;
		this.price = null;
	}
}
</script>
<style lang="scss" scoped>
.add-item-container {
    display: flex;
    justify-content: space-around;
    margin-left: 250px;
    margin-right: 250px;
    .input {
			background: none;
			border: 2px solid lightseagreen;
			color: black;
			font-weight: bold;
			font-size: 18px;
			height: 50px;
			width: 150px;
			border-radius: 2px;
			margin-left: 15px;
			margin-right: 15px;
			text-align: center;

			&.empty {
				border: 2px solid lightgray;
			}
    }

    .submit {
        border: 2px solid green;
        border-radius: 5px;
        width: 100px;
        height: 50px;
        background: none;
        font-weight: bold;
        font-size: 18px;

        &:hover {
            border: 2px solid lightseagreen;
            background: lightgreen;
            cursor: pointer;
        }
        &.disabled {
            border: 2px solid red;
            color: darkgrey;
            background: lightgrey;
        }
    }
}
</style>