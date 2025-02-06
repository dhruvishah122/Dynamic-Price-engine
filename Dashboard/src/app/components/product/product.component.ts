import { NgClass } from '@angular/common';
import { Component, ViewChild, ElementRef  } from '@angular/core';
import { FormsModule } from '@angular/forms'; 
import Swal from 'sweetalert2';
import { NgbModule} from '@ng-bootstrap/ng-bootstrap';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { HttpClientModule } from '@angular/common/http';
@Component({
  selector: 'app-product',
  imports: [FormsModule,NgbModule,ReactiveFormsModule,HttpClientModule],
  templateUrl: './product.component.html',
  styleUrl: './product.component.css'
})
export class ProductComponent {
  constructor(private http: HttpClient) {}

  selectedFile: File | null = null;
  @ViewChild('exampleModal') myModal: ElementRef | undefined;

  onFileSelect(event: Event): void {
    const input = event.target as HTMLInputElement;
    
    // Check if files were selected
    if (input && input.files && input.files.length > 0) {
      this.selectedFile = input.files[0];  // Select the first file
      console.log('File selected:', this.selectedFile);
    } else {
      console.log('No file selected');
    }
    }
    showModal: boolean = false;

  formData={
    name:'',
    price:'',
    desc:'',
    sku:'',
    brand:'',
    selectedOption: '',
    selectedFile:''
    }
    onBackdropClick(event: MouseEvent) {
      const target = event.target as HTMLElement;
      if (target.classList.contains('modal')) {
        this.closeModal();
      }
    }
  
    closeModal() {
      this.showModal = false;
    }
  
    
 onSubmit(){

if(this.formData.desc!=''&&this.formData.brand!='',this.formData.name!=''&&this.formData.price!=''&&this.formData.sku!=''&&this.formData.selectedOption!='' && this.selectedFile!=null) {
  const apiUrl = 'http://localhost:8081/addProduct'; // Update with your endpoint
console.log(this.formData);
    this.http.post(apiUrl, this.formData).subscribe({
      next: (response) => {
        console.log('Form data submitted successfully:', response);
        Swal.fire({
          title: 'Success!',
          text: 'The action was successful.',
          icon: 'success',
          confirmButtonText: 'Ok'
        });
      },
      error: (error) => {
        console.error('Error submitting form:', error);
        Swal.fire({
          title: 'Fail!',
          text: 'The action was failed.',
          icon: 'error',
          confirmButtonText: 'Ok'
        });
      },
    });
 
}
else{
  Swal.fire({
    title: 'Fail!',
    text: 'The action was failed.',
    icon: 'error',
    confirmButtonText: 'Ok'
  });
}   this.closeModal();
  }
}
