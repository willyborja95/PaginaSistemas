import { Component, OnInit } from '@angular/core';
import { ItemCategoryService } from '../../services/itemCategory.service';
import { CategoryService } from '../../services/category.service';
import { Category } from '../../models/category';
import { ItemCategory } from '../../models/itemCategory';
import { FormGroup, FormControl, Validators, AbstractControl } from '@angular/forms';

@Component({
  selector: 'app-itemcategory',
  templateUrl: './itemcategory.component.html',
  styleUrls: ['./itemcategory.component.css']
})
export class ItemcategoryComponent implements OnInit {

  listCategories: Category[] = [];
  listItemCategories: ItemCategory[] = [];
  itemCategoryForm: FormGroup;

  constructor(
    private itemCategoryService: ItemCategoryService,
    private categoryService: CategoryService,
  ) {
    this.itemCategoryForm = this.createFormGroup();

  }

  updateListCategories() {
    this.categoryService.getCategories().subscribe(categories => {
      this.listCategories = categories;
    });
  }

  updateListItemCategories() {
    this.itemCategoryService.getItemCategories().subscribe(itemCategories => {
      this.listItemCategories = itemCategories
    },
      error => {
        alert(JSON.stringify(error));
      }
    );
    //alert("holas")
  }

  deleteItemCategory(id: number) {
    this.itemCategoryService.deleteItemCategory(id).subscribe(categories => {
      this.updateListItemCategories();
    },
      error => {
        alert(JSON.stringify(error));
      })

  }

  /*

  

  updateCategory(id: number) {
    alert(JSON.stringify(this.itemCategoryForm.valueChanges));
  }
  */
  public ngOnInit() {
    this.updateListCategories();
    this.updateListItemCategories();
  }

  displayedColumns: string[] = ['nameItemCategory', 'active', 'category', 'delete', 'update'];

  //FORM ACTIONS
  //Create new form
  createFormGroup() {
    return new FormGroup({
      idItemCategory: new FormControl(),
      nameItemCategory: new FormControl('', [
        Validators.required,
        Validators.maxLength(15)
      ]),
      active: new FormControl(false),
      category: new FormControl()
    });
  }

  /*
  //Load data in form
  loadData(categoryEdit: Category) {
    this.itemCategoryForm.setValue({
      idCategory: categoryEdit.idCategory,
      nameCategory: categoryEdit.nameCategory,
      active: categoryEdit.active,
    })
  }
  */
  //submit form
  submitForm() {
    if (this.itemCategoryForm.value.idItemCategory == null) {
      if (this.itemCategoryForm.valid) {
        this.itemCategoryService.createItemCategory(this.itemCategoryForm.value).subscribe(category => {
          this.updateListItemCategories();
        }, error => {
          alert(JSON.stringify(error));
        })
        this.resetForm();
      }
    }
    /*
    else {
      if (this.itemCategoryForm.valid) {
        this.itemCategoryService.updateCategory(this.itemCategoryForm.value).subscribe(category => {
          this.updateListCategories();
        })
        this.resetForm();
      }
    }
    */
  }

  //reset form
  resetForm() {
    let control: AbstractControl = null;
    this.itemCategoryForm.reset({ active: false });
    this.itemCategoryForm.markAsUntouched();
    Object.keys(this.itemCategoryForm.controls).forEach((nameControl) => {
      control = this.itemCategoryForm.controls[nameControl];
      control.setErrors(null);
    });
  }

}
