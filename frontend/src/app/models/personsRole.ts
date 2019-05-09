import { ItemCategory } from './itemCategory';
//import { Persons } from './persons';

export class PersonsRole {

    idPersonsRole: number;
    itemCategory: ItemCategory;
    //person : Persons;

    constructor(idPersonsRole?: number, itemCategory?: ItemCategory){
        this.idPersonsRole = idPersonsRole,
        this.itemCategory = itemCategory
        //this.person = person
    }

}