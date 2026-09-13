#!/bin/bash
# 移除 Gemini News Bot Service 和 Timer

echo "🗑️  正在移除 Gemini News Bot Service..."

# 停止並停用 timer
echo "⏹️  停止 timer..."
sudo systemctl stop gemini-news-bot.timer
sudo systemctl disable gemini-news-bot.timer

# 停止 service (如果正在執行)
sudo systemctl stop gemini-news-bot.service 2>/dev/null

# 移除 systemd 檔案
echo "🗑️  移除系統檔案..."
sudo rm -f /etc/systemd/system/gemini-news-bot.service
sudo rm -f /etc/systemd/system/gemini-news-bot.timer

# 重新載入 systemd 配置
echo "🔄 重新載入 systemd 配置..."
sudo systemctl daemon-reload
sudo systemctl reset-failed

echo ""
echo "✅ 移除完成！服務已完全停止並移除。"
echo ""
echo "📊 驗證移除結果："
sudo systemctl list-unit-files | grep gemini-news-bot || echo "✓ 沒有找到相關服務檔案 (移除成功)"