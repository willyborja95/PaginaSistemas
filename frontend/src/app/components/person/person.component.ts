import { Component, OnInit } from '@angular/core';
import { Person } from '../../models/person';
import { PersonService } from '../../services/person.service';
import { FormGroup, FormControl, Validators, AbstractControl } from '@angular/forms';


@Component({
  selector: 'app-person',
  templateUrl: './person.component.html',
  styleUrls: ['./person.component.css']
})
export class PersonComponent implements OnInit {
  listPersons: Person[] = [];
  personForm: FormGroup;
  constructor(
    private personServices: PersonService
  ) { 
    this.personForm = this.createFormGroup();
  }
  updateListPersons() {
    this.personServices.getPersons().subscribe(person => {
      this.listPersons = person;
    })
  }
  deletePersons(name: string) {
    this.personServices.deletePersons(name).subscribe(person => {
    },
      error => {
        alert(JSON.stringify(error));
      })
    this.updateListPersons();
  }

  ngOnInit() {
    this.updateListPersons();
  }
  displayedColumns: string[] = ['first_name', 'second_name','first_last_name','second_last_name', 'delete', 'update'];
 //FORM ACTIONS
  //Create new form
  createFormGroup() {
    return new FormGroup({
      
      first_name: new FormControl('', [
        Validators.required,
        Validators.maxLength(255)
      ]),
      second_name: new FormControl('', [
        Validators.required,
        Validators.maxLength(255)
      ]),
      first_last_name: new FormControl('', [
        Validators.required,
        Validators.maxLength(255)
      ]),
      second_last_name: new FormControl('', [
        Validators.required,
        Validators.maxLength(255)
      ]),
   
    });
  }
   //Load data in form
   loadData(personsEdit: Person) {
    this.personForm.setValue({
     
      first_name: personsEdit.first_name,
      second_name: personsEdit.second_name,
      first_last_name:personsEdit.first_last_name,
      second_last_name:personsEdit.second_last_name
      
    })
  }
  //submit form
  submitForm() {
    if (this.personForm.value.first_name == null) {
      if (this.personForm.valid) {
        this.personServices.createPersons(this.personForm.value).subscribe(person => {
          this.updateListPersons();
        })
        this.resetForm();
      }
    }else{
      if (this.personForm.valid) {
        this.personServices.updatePersons(this.personForm.value).subscribe(person => {
          this.updateListPersons();
        })
        this.resetForm();
      }
    }

    
  }
  //reset form
  resetForm() {
    let control: AbstractControl = null;
   
    this.personForm.markAsUntouched();
    Object.keys(this.personForm.controls).forEach((nameControl) => {
      control = this.personForm.controls[nameControl];
      control.setErrors(null);
    });
    this.personForm.reset;
  }
}
