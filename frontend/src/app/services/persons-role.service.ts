import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { PersonsRole } from '../models/personsRole';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class PersonsRoleService {
  private apiUrl: string;

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  }
  
  constructor(private httpClient: HttpClient,
    ) {
      this.apiUrl = environment.apiUrl;
  
    }

    public createPersonsRole(personsRole: PersonsRole) {
      return this.httpClient.post(this.apiUrl+'personsrole/', personsRole, this.httpOptions);
    }

    public updatePersonsRole(personsRole: PersonsRole) {
      return this.httpClient.put(this.apiUrl+'personsrole/'+personsRole.idPersonsRole+'/', personsRole,this.httpOptions);
    }

    public deletePersonsRole(id: number) { 
      return this.httpClient.delete(this.apiUrl+'personsrole/'+id+'/', this.httpOptions);
    }

    public getPersonsRole() { 
      return this.httpClient.get<PersonsRole[]>(this.apiUrl+'personsrole', this.httpOptions);
    }
}
