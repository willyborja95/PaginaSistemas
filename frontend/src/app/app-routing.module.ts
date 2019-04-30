import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CategoryComponent } from './components/category/category.component';
import { ItemcategoryComponent } from './components/itemcategory/itemcategory.component';

const routes: Routes = [
  { path: 'category', component: CategoryComponent },
  { path: 'itemcategory', component: ItemcategoryComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
