import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule, HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  trashCans = [
    { id: 1, title: 'Title', boxes: [
      'Cardboard', 'Food Organics', 'Glass', 'Metal', 'Miscellaneous Trash',
      'Paper', 'Plastic', 'Textile Trash', 'Vegetation'
    ], highlight: false }
  ];
  box_to_highlight = '';
  nextId = 2;
  draggedItem: string = '';
imagePreview: string | ArrayBuffer | null = null;

  constructor(private http: HttpClient) {}

  addTrashCan() {
    this.trashCans.push({ id: this.nextId++, title: 'Title', boxes: [], highlight: false });
  }

  onDragStart(item: string) {
    this.draggedItem = item;
  }

  onDrop(can: any) {
    const item = this.draggedItem;
    if (item && !can.boxes.includes(item)) {
      const sourceCan = this.trashCans.find(tc => tc.boxes.includes(item));
      if (sourceCan) {
        sourceCan.boxes = sourceCan.boxes.filter(b => b !== item);
      }
      can.boxes.push(item);
    }
    this.draggedItem = '';
  }

  allowDrop(event: Event) {
    event.preventDefault();
  }

  onFileSelected(event: any) {
    const file = event.target.files[0];
   
    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        this.imagePreview = reader.result;
      };
      reader.readAsDataURL(file);

      const formData = new FormData();
      formData.append('file', file);

      this.http.post<{ prediction: string }>('http://127.0.0.1:5000/predict', formData).subscribe(
        (res) => {
          console.log('Prediction response:', res);
          this.highlightContainer(res.prediction);
        },
        (err) => console.error('Upload error', err)
      );
    }
  }

  highlightContainer(label: string) {
    this.box_to_highlight = label;
    this.trashCans.forEach(can => {
      can.highlight = can.boxes.includes(label);

    });
  }
}