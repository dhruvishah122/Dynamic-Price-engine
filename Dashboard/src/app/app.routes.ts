import { Routes } from '@angular/router';
import { RouterModule } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import {ProductComponent} from "./components/product/product.component";
import { CompetitorComponent } from './components/competitor/competitor.component';
import { InventoryComponent } from './components/inventory/inventory.component';
import { PricingComponent } from './components/pricing/pricing.component';
import { NgModule } from '@angular/core';
export const routes: Routes = [
    { path: '', redirectTo: '/home', pathMatch: 'full' }, // Default route
    { path: 'home', component: HomeComponent },
    { path: 'products', component: ProductComponent },
    { path: 'competitor', component: CompetitorComponent },
    { path: 'inventory', component: InventoryComponent },
    { path: 'pricing', component: PricingComponent }
];
@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule],
  })
  export class AppRoutingModule {}