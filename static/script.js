document.addEventListener('DOMContentLoaded', () => {
  const recordBtn = document.getElementById('record-btn');
  let mediaRecorder;
  let audioChunks = [];

  recordBtn.addEventListener('click', async () => {
      if (mediaRecorder && mediaRecorder.state === 'recording') {
          mediaRecorder.stop();
          recordBtn.textContent = 'Record';
      } else {
          const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
          mediaRecorder = new MediaRecorder(stream);

          mediaRecorder.ondataavailable = event => {
              audioChunks.push(event.data);
              if (mediaRecorder.state === 'inactive') {
                  const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
                  audioChunks = [];
                  sendAudioData(audioBlob);
              }
          };

          mediaRecorder.start();
          recordBtn.textContent = 'Stop';
      }
  });

  const sendAudioData = async (audioBlob) => {
      const formData = new FormData();
      formData.append('audio', audioBlob);

      const response = await fetch('/transcribe', {
          method: 'POST',
          body: formData
      });

      const result = await response.json();
      document.getElementById('transcript').textContent = result.transcript;
      document.getElementById('response').textContent = result.message;
  };
});
