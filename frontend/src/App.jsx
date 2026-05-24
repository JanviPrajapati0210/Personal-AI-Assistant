import { useEffect, useState } from "react";

function App() {

  const [message, setMessage] = useState("");

  const [chat, setChat] = useState([]);

  const [chats, setChats] = useState([]);

  const [currentChatId, setCurrentChatId] =
    useState(null);

  // Load chats on startup
  useEffect(() => {
    loadChats();
  }, []);

  // Load all chats
  const loadChats = async () => {

    const response = await fetch(
      "http://127.0.0.1:8000/chats"
    );

    const data = await response.json();

    setChats(data.chats);

    // Auto open first chat
    if (data.chats.length > 0 && !currentChatId) {

      const firstChatId =
        data.chats[0][0];

      openChat(firstChatId);
    }
  };

  // Create new chat
  const createNewChat = async () => {

    const response = await fetch(
      "http://127.0.0.1:8000/chat/new",
      {
        method: "POST"
      }
    );

    const data = await response.json();

    await loadChats();

    openChat(data.chat_id);
  };

  // Open chat
  const openChat = async (chatId) => {

    setCurrentChatId(chatId);

    const response = await fetch(
      `http://127.0.0.1:8000/chat/${chatId}`
    );

    const data = await response.json();

    setChat(data.messages);
  };

  // Send message
  const sendMessage = async () => {

    if (!message.trim()) return;

    const userMessage = {
      role: "user",
      content: message
    };

    setChat(prev => [...prev, userMessage]);

    const currentMessage = message;

    setMessage("");

    const response = await fetch(
      "http://127.0.0.1:8000/chat",
      {
        method: "POST",

        headers: {
          "Content-Type": "application/json"
        },

        body: JSON.stringify({
          chat_id: currentChatId,
          message: currentMessage
        })
      }
    );

    const data = await response.json();

    const aiMessage = {
      role: "assistant",
      content: data.response
    };

    setChat(prev => [...prev, aiMessage]);

    loadChats();
  };

  return (

    <div className="flex h-screen bg-gray-900 text-white">

      {/* Sidebar */}
      <div className="w-64 bg-gray-800 p-4 flex flex-col">

        <button
          onClick={createNewChat}
          className="bg-blue-600 p-3 rounded-lg mb-4"
        >
          + New Chat
        </button>

        <div className="flex-1 overflow-y-auto space-y-2">

          {chats.map((chatItem) => (

            <div
              key={chatItem[0]}
              onClick={() =>
                openChat(chatItem[0])
              }
              className={`p-3 rounded-lg cursor-pointer ${
                currentChatId === chatItem[0]
                  ? "bg-blue-600"
                  : "bg-gray-700"
              }`}
            >
              {chatItem[1]}
            </div>

          ))}

        </div>

      </div>

      {/* Main Chat Area */}
      <div className="flex-1 flex flex-col">

        <div className="p-4 border-b border-gray-700 text-2xl font-bold">
          AI Assistant
        </div>

        <div className="flex-1 overflow-y-auto p-4 space-y-4">

          {chat.map((msg, index) => (

            <div
              key={index}
              className={`p-3 rounded-xl max-w-xl whitespace-pre-wrap ${
                msg.role === "user"
                  ? "bg-blue-600 ml-auto"
                  : "bg-gray-700"
              }`}
            >
              {msg.content}
            </div>

          ))}

        </div>

        <div className="p-4 border-t border-gray-700 flex gap-2">

          <input
            type="text"
            placeholder="Type a message..."
            value={message}
            onChange={(e) =>
              setMessage(e.target.value)
            }
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                sendMessage();
              }
            }}
            className="flex-1 p-3 rounded-lg bg-gray-800 outline-none"
          />

          <button
            onClick={sendMessage}
            className="bg-blue-600 px-6 rounded-lg"
          >
            Send
          </button>

        </div>

      </div>

    </div>
  );
}

export default App;