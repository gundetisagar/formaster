from dataclasses import dataclass
from typing import List


@dataclass()
class SubCategoryDto:
    sub_category_id: int
    sub_category: str

@dataclass()
class CategoryDto:
    category_id: int
    category: str
    sub_category_list: List[SubCategoryDto]
