import cv2
from ultralytics import YOLO

def main():
    # モデルの読み込み
    model = YOLO(r'C:\Users\041674\VSCode\YOLOv8\ultralytics\runs\detect\crg_epochs_10\weights\best.pt')  # run_nameを適切に置き換えてください

    # Webカメラの初期化
    cap = cv2.VideoCapture(0)  # 0はデフォルトのカメラを指定

    # 信頼度のしきい値
    CONFIDENCE_THRESHOLD = 0.9

    while True:
        # フレームの読み込み
        ret, frame = cap.read()
        if not ret:
            break

        # 物体検出の実行
        results = model(frame)

        # 結果の描画
        for result in results:
            boxes = result.boxes.cpu().numpy()
            for box in boxes:
                confidence = box.conf[0]
                
                # 信頼度がしきい値以上の場合のみ描画
                if confidence >= CONFIDENCE_THRESHOLD:
                    x1, y1, x2, y2 = box.xyxy[0].astype(int)
                    class_id = box.cls[0]

                    # バウンディングボックスの描画
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                    # クラス名と信頼度の表示
                    label = f"{model.names[int(class_id)]}: {confidence:.2f}"
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # 結果の表示
        cv2.imshow('YOLOv8 Detection', frame)

        # 'q'キーで終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # リソースの解放
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()