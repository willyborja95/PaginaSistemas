import { Component, OnInit } from '@angular/core';
import { ItemCategoryService } from '../../services/itemCategory.service';
import { PersonsRoleService  } from '../../services/persons-role.service';
//import { CategoryService } from '../../services/category.service';

//import { Category } from '../../models/category';
//import { Persons } from '../../models/persons';
import { ItemCategory } from '../../models/itemCategory';
import { PersonsRole } from '../../models/personsRole';
import { FormGroup, FormControl, Validators, AbstractControl } from '@angular/forms';

@Component({
  selector: 'app-personsrole',
  templateUrl: './personsrole.component.html',
  styleUrls: ['./personsrole.component.css']
})
export class PersonsroleComponent implements OnInit {

  //listPersons: Persons[] = [];
  listItemCategories: ItemCategory[] = [];
  personsRoleForm: FormGroup;

  constructor(
    //private personsRoleService: PersonsRoleService ,
    //private personsService: PersonService,
    private itemCategoryService: ItemCategoryService,
  ) {
    this.personsRoleForm = this.createFormGroup();
   }

   updateListItemCategories() {
    this.itemCategoryService.getItemCategories().subscribe(itemCategories => {
      this.listItemCategories = itemCategories
    },
      error => {
        alert(JSON.stringify(error));
      }
    );
  }

  ngOnInit() {
    //this.updateListCategories();
    this.updateListItemCategories();
  }

  createFormGroup() {
    return new FormGroup({
      idPersonsRole: new FormControl(),
      nameItemCategory: new FormControl('', [
        Validators.required,
        Validators.maxLength(255)
      ]),
      active: new FormControl(false),
      category: new FormControl('', [
        Validators.required,
      ])
    });
  }

  //submit form
  /*submitForm() {
    if (this.personsRoleForm.value.idItemCategory == null) {
      if (this.personsRoleForm.valid) {
        this.itemCategoryService.createItemCategory(this.itemCategoryForm.value).subscribe(category => {
          this.updateListItemCategories();
        }, error => {
          alert(JSON.stringify(error));
        })
        this.resetForm();
      }
    }
    else {
      if (this.itemCategoryForm.valid) {
        this.itemCategoryService.updateItemCategory(this.itemCategoryForm.value).subscribe(category => {
          this.updateListItemCategories();
        })
        this.resetForm();
      }
    }
  }
*/

  //reset form
  resetForm() {
    let control: AbstractControl = null;
    this.personsRoleForm.reset({ active: false });
    this.personsRoleForm.markAsUntouched();
    Object.keys(this.personsRoleForm.controls).forEach((nameControl) => {control = this.personsRoleForm.controls[nameControl];
      control.setErrors(null);
    });
  }
}
