class ShoppingTool:
    def create_shopping_list(self, meals):
        items = []
        for meal in meals:
            items.extend(meal.get("ingredients", []))
        return list(set(items))
