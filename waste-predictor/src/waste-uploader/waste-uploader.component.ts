import { Component } from '@angular/core';
import { WastePredictionService } from '../services/waste-prediction.service'; 

@Component({
  selector: 'app-waste-uploader',
  imports: [],
  templateUrl: './waste-uploader.component.html',
  styleUrl: './waste-uploader.component.css'
})

export class WasteUploaderComponent {
  selectedFile!: File;
  prediction: string | null = null;

  constructor(private wasteService: WastePredictionService) {}

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  predict() {
    if (!this.selectedFile) return;

    this.wasteService.sendImage(this.selectedFile).subscribe(
      response => this.prediction = response.prediction,
      error => console.error('Error:', error)
    );
  }
}
