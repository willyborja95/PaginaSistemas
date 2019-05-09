import { Person } from './person';
import { ItemCategory } from './itemCategory';

export class PersonsRole {

    idPersonsRole: number;
    person : Person;
    itemCategory: ItemCategory;

    constructor(idPersonsRole?: number, person?: Person, itemCategory?: ItemCategory){
        this.idPersonsRole = idPersonsRole,
        this.person = person,
        this.itemCategory = itemCategory  
    }

}