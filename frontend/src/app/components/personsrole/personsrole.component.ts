import { Component, OnInit } from '@angular/core';
import { ItemCategoryService } from '../../services/itemCategory.service';
import { CategoryService } from '../../services/category.service';
import { Category } from '../../models/category';
import { ItemCategory } from '../../models/itemCategory';
import { FormGroup, FormControl, Validators, AbstractControl } from '@angular/forms';

@Component({
  selector: 'app-personsrole',
  templateUrl: './personsrole.component.html',
  styleUrls: ['./personsrole.component.css']
})
export class PersonsroleComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
