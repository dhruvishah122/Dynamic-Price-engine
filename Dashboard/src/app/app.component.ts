import { NgClass } from '@angular/common';
import { Component, ElementRef, NgModule, ViewChild } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { FormsModule } from '@angular/forms'; 
@Component({
  selector: 'app-root',
  imports: [RouterOutlet,RouterLink,NgClass],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Dashboard';
  isNavbarCollapsed = true;
  background:string="45aef1";
  clickedMenuItem: string = '';

  onMenuClick(menuName: string) {
    this.clickedMenuItem = menuName; // Set the clicked menu item
  }

 
}
